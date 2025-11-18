# iac/terraform/cloudfront.tf

# -------------------------
# Origin Access Identity (OAI)
# -------------------------

resource "aws_cloudfront_origin_access_identity" "qwik_fe_bucket_oai" {
  comment = "OAI for QWiK Frontend Bucket"
}
