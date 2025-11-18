# iac/terraform/outputs.tf

output "qwik_frontend_url" {
  description = "The domain name of the QWiK Frontend CDN"
  # 생성된 CloudFront의 도메인 이름을 출력
  value = "https://${aws_cloudfront_distribution.qwik_frontend_cdn.domain_name}"
}
