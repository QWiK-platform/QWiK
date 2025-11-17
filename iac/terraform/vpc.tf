# iac/terraform/vpc.tf

# VPC (10.0.0.0/16)
resource "aws_vpc" "qwik_vpc" {
  # CIDR Block 설정
  cidr_block = "10.0.0.0/16"

  # DNS 설정
  enable_dns_support = true
  enable_dns_hostnames = true

  tags = {
    Name = "QWiK-VPC"
  }
}

# Subnets

# -------------------------
# AZ 1 (ap-northeast-2a)
# -------------------------

# Public Subnet (10.0.1.0/24)
resource "aws_subnet" "qwik_public_subnet_az1" {
  # VPC에 연결
  vpc_id = aws_vpc.qwik_vpc.id
  
  # CIDR Block 설정
  cidr_block = "10.0.1.0/24"

  # AZ 설정
  availability_zone = "ap-northeast-2a"

  # Public IP
  map_public_ip_on_launch = true

  tags = {
    Name = "QWiK-Public-Subnet-AZ1"
  }
}

# Private Subnet (10.0.11.0/24)
resource "aws_subnet" "qwik_private_subnet_az1" {
  # VPC에 연결
  vpc_id = aws_vpc.qwik_vpc.id
  
  # CIDR Block 설정
  cidr_block = "10.0.11.0/24"

  # AZ 설정
  availability_zone = "ap-northeast-2a"

  tags = {
    Name = "QWiK-Private-Subnet-AZ1"
  }
}

# -------------------------
# AZ 2 (ap-northeast-2b)
# -------------------------

# Public Subnet (10.0.2.0/24)
resource "aws_subnet" "qwik_public_subnet_az2" {
  # VPC에 연결
  vpc_id = aws_vpc.qwik_vpc.id
  
  # CIDR Block 설정
  cidr_block = "10.0.2.0/24"

  # AZ 설정
  availability_zone = "ap-northeast-2b"

  # Public IP
  map_public_ip_on_launch = true

  tags = {
    Name = "QWiK-Public-Subnet-AZ2"
  }
}

# Private Subnet (10.0.12.0/24)
resource "aws_subnet" "qwik_private_subnet_az2" {
  # VPC에 연결
  vpc_id = aws_vpc.qwik_vpc.id
  
  # CIDR Block 설정
  cidr_block = "10.0.12.0/24"

  # AZ 설정
  availability_zone = "ap-northeast-2b"

  tags = {
    Name = "QWiK-Private-Subnet-AZ2"
  }
}

# -------------------------
# AZ 3 (ap-northeast-2c)
# -------------------------

# Public Subnet (10.0.3.0/24)
resource "aws_subnet" "qwik_public_subnet_az3" {
  # VPC에 연결
  vpc_id = aws_vpc.qwik_vpc.id
  
  # CIDR Block 설정
  cidr_block = "10.0.3.0/24"

  # AZ 설정
  availability_zone = "ap-northeast-2c"

  # Public IP
  map_public_ip_on_launch = true

  tags = {
    Name = "QWiK-Public-Subnet-AZ3"
  }
}

# Private Subnet (10.0.13.0/24)
resource "aws_subnet" "qwik_private_subnet_az3" {
  # VPC에 연결
  vpc_id = aws_vpc.qwik_vpc.id
  
  # CIDR Block 설정
  cidr_block = "10.0.13.0/24"

  # AZ 설정
  availability_zone = "ap-northeast-2c"

  tags = {
    Name = "QWiK-Private-Subnet-AZ3"
  }
}

