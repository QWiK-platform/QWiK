# iac/compute/iam.tf

# IAM Role 생성
resource "aws_iam_role" "k8s_ssm_role" {
  name = "QWiK-K8s-SSM-Role-${var.environment}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
    }]
  })

  tags = {
    Name        = "QWiK-K8s-SSM-Role-${var.environment}"
    Environment = var.environment
  }
}

# SSM 접속용 정책 연결
resource "aws_iam_role_policy_attachment" "ssm_core" {
  role       = aws_iam_role.k8s_ssm_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

# ECR 읽기 권한 연결
resource "aws_iam_role_policy_attachment" "ecr_read" {
  role       = aws_iam_role.k8s_ssm_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

# 인스턴스 프로파일
resource "aws_iam_instance_profile" "k8s_ssm_profile" {
  name = "QWiK-K8s-SSM-Profile-${var.environment}"
  role = aws_iam_role.k8s_ssm_role.name
}
