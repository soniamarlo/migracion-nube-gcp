terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.38.0"
    }
  }
}

provider "google" {
  # Configuration options
    project = "x-victor-428120-c7"
    region = "europe-west3"
    zone = "europe-west3-b"
    credentials = file("cred.json")
}

resource "google_compute_network" "tareafinal-vpc" {
    name = "nueva-vpc"
    project = "x-victor-428120-c7"
    description = "red virtual para proyecto final"
    auto_create_subnetworks = true
}

resource "google_compute_address" "tareafinal-ip" {
    name = "nueva-ip"
    project = "x-victor-428120-c7"
}

resource "google_compute_firewall" "allow-ssh" {
  name    = "allow-ssh"
  network = google_compute_network.tareafinal-vpc.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["ssh-server"]
}
resource "google_compute_firewall" "allow-http" {
  name    = "allow-http"
  network = google_compute_network.tareafinal-vpc.name

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["http-server"]
}
resource "random_integer" "random" {
  min = 0
  max = 50
}

resource "google_storage_bucket" "bucket" {
  name          = "tareafinal-1-${random_integer.random.result}"
  location      = "EU"
  project = "x-victor-428120-c7"
  force_destroy = true
  storage_class = "NEARLINE"
  uniform_bucket_level_access = "true"

}


resource "google_service_account" "tareafinal-sa" {
  account_id   = "mi-tareafinal-sa"
  display_name = "Mi cuenta servicio para VM"
}

resource "google_compute_instance" "tareafinal-instancia" {
    name         = "nueva-instancia"
    machine_type = "n2-standard-2"
    zone         = "europe-west3-b"
    tags = ["ssh-server", "http-server", "foo","bar"] 
    
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
      type  = "pd-standard"
    }
  }

   network_interface {
    network    = google_compute_network.tareafinal-vpc.self_link
    access_config {
      // IP Efímera
    }

  }
   metadata = {
    foo = "bar"
  }

  metadata_startup_script = "echo Hola, soy la instancia de prueba de Sonia > /test.txt"
  

   service_account {
    email  = google_service_account.tareafinal-sa.email
    scopes = ["cloud-platform"]
  }
  
}