module "security_group" {
  source  = "terraform-aws-modules/security-group/aws"
  version = "3.18.0"

  name        = "artifactory-sg"
  description = "Security group for Artifactory"
  vpc_id      = module.vpc.vpc_id

  ingress_cidr_blocks = ["0.0.0.0/0"]
  ingress_rules       = ["http-8081-tcp"]
}