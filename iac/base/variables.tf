# iac/base/variables.tf

variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "ap-northeast-2" # 서울 리전
}

variable "qwik_frontend_bucket_name" {
  description = "프론트엔드 버킷명"
  type = string
  default = "qwik-frontend-bucket-2025"
}
