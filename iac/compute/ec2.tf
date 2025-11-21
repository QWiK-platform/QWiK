# iac/compute/ec2.tf

# 최신 우분투 AMI 찾기
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# Master Node
resource "aws_instance" "k8s_master" {
  ami                  = data.aws_ami.ubuntu.id
  instance_type        = "t3.medium"
  
  # Private Subnet 1번 사용
  subnet_id            = data.terraform_remote_state.base.outputs.private_subnet_ids[0]
  
  # SSM 권한 부여
  iam_instance_profile = aws_iam_instance_profile.k8s_ssm_profile.name 
  associate_public_ip_address = false
  
  vpc_security_group_ids = [
    aws_security_group.k8s_internal.id,
    aws_security_group.k8s_external.id
  ]

  tags = {
    Name        = "QWiK-K8s-Master-${var.environment}"
    Role        = "master"
    Environment = var.environment
  }
}

# Worker Node
resource "aws_instance" "k8s_worker" {
  ami                  = data.aws_ami.ubuntu.id
  instance_type        = "t3.medium"
  
  # Private Subnet 1번 사용 (같은 AZ)
  subnet_id            = data.terraform_remote_state.base.outputs.private_subnet_ids[0]
  
  # SSM 권한 부여
  iam_instance_profile = aws_iam_instance_profile.k8s_ssm_profile.name 
  associate_public_ip_address = false
  
  vpc_security_group_ids = [
    aws_security_group.k8s_internal.id,
    aws_security_group.k8s_external.id
  ]

  tags = {
    Name        = "QWiK-K8s-Worker-${var.environment}"
    Role        = "worker"
    Environment = var.environment
  }
}

# 접속용 ID 출력 (SSM 접속 시 필요)
output "master_instance_id" { value = aws_instance.k8s_master.id }
output "worker_instance_id" { value = aws_instance.k8s_worker.id }
