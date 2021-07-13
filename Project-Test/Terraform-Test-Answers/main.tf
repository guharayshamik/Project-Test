 # Ans: a : Take a snapshot of an existing ubuntu VM on a given vsphere server
 # Creating VM with below configurations 
provider "vsphere" {
  vsphere_server = var.vsphere_server
  user           = var.vsphere_user
  password       = var.vsphere_password

  # If you have a self-signed cert
  allow_unverified_ssl = true
}

data "vsphere_datacenter" "dc" {
  name = "${var.datacenter}"
}

data "vsphere_virtual_machine" "ubuntu" {
  name          = "/${var.datacenter}/vm/${var.ubuntu_name}"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_network" "network" {
  name          = "public"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_compute_cluster" "cluster" {
  name          = "${var.cluster}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_datastore" "datastore" {
  name          = "${var.datastore}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

resource "vsphere_virtual_machine" "new_vm" {
  name             = "new_vm-prov"
  resource_pool_id = data.vsphere_compute_cluster.cluster.resource_pool_id
  datastore_id     = data.vsphere_datastore.datastore.id

  num_cpus = 4
  memory   = 8192

  network_interface {
    network_id = data.vsphere_network.network.id
  }

  wait_for_guest_net_timeout = -1
  wait_for_guest_ip_timeout  = -1

  disk {
    label = "disk0"
    thin_provisioned = true
  }
  guest_id = "ubuntu64Guest"

  clone {
    template_uuid = data.vsphere_virtual_machine.ubuntu.id
  }
}
resource "vsphere_virtual_disk" "my_disk" {
  size       = 120
  vmdk_path  = "${var.vm_path}/my_disk.vmdk"
  datacenter = var.datacenter
  datastore  = var.datastore
  type       = "thin"
}


#Ans: a : Take a snapshot of an existing ubuntu VM on a given vsphere server
resource "vsphere_virtual_machine_snapshot" "new_snap" {
  virtual_machine_uuid = vsphere_virtual_machine.new_vm.id
  snapshot_name        = "snap-tf-ubuntu"
  description          = "Created using Terraform"
  memory               = "true"
  quiesce              = "true"
  remove_children      = "false"
  consolidate          = "true"
}
output "vm_ip" {
  value = vsphere_virtual_machine.new_vm.guest_ip_addresses
}