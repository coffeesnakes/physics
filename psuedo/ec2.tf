module "ec2" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "2.16.0"

  name          = "artifactory-instance"
  instance_count = 1

  ami                    = "ami-0c94855ba95c574c8" # This should be the ID of an AMI that has Artifactory pre-installed
  instance_type          = "t2.medium"
  key_name               = "your-key-name"
  subnet_id              = module.vpc.public_subnets[0]
  vpc_security_group_ids = [module.security_group.this_security_group_id]

  tags = {
    Name = "artifactory-instance"
  }
}