variable "instance_profile_name" {
  type    = string
  default = "jenkins-instance-profile"
}

variable "iam_policy_name" {
  type    = string
  default = "jenkins-policy"
}

variable "role_name" {
  type    = string
  default = "jenkins-role"
}