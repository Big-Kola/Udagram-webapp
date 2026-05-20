output "alb_dns" {
  value = aws_lb.app_lb.dns_name
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.udagram_cluster.name
}

output "rds_endpoint" {
  value = aws_db_instance.udagram_db.address
}

output "vpc_id" {
  value = aws_vpc.udagram_vpc.id
}
