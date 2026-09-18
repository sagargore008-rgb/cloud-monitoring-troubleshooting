# Cloud Monitoring & Troubleshooting System

## Overview

A cloud monitoring and troubleshooting project that monitors a
Dockerized application running on AWS EC2.

The system collects CPU, memory, disk, and application log data using
Amazon CloudWatch and generates alerts when resource usage crosses
defined thresholds.

## Architecture

GitHub
   ↓
Dockerized Flask Application
   ↓
AWS EC2
   ↓
CloudWatch Agent
   ├── CPU Metrics
   ├── Memory Metrics
   ├── Disk Metrics
   └── Application Logs
          ↓
     CloudWatch
          ↓
       Alarms
          ↓
         SNS
          ↓
      Email Alert

## Technologies

- AWS EC2
- Amazon CloudWatch
- CloudWatch Agent
- Amazon SNS
- Docker
- Python
- Flask
- Linux
- Git & GitHub

## Monitoring

The project monitors:

- CPU utilization
- Memory utilization
- Disk utilization
- Application logs
- Application health

## Alerts

Configured CloudWatch alarms for:

- High CPU usage
- High memory usage
- High disk usage

SNS is used for email notifications.

## Troubleshooting Scenarios

### 1. Container Failure

Stopped the Docker container intentionally and investigated the issue
using Docker commands.

Commands:

docker ps -a
docker logs monitoring-app
docker start monitoring-app

### 2. Application Error

Generated an HTTP 500 error and inspected application logs.

curl http://localhost:5000/error

### 3. High CPU

Generated CPU load using stress-ng and monitored the CloudWatch alarm.

stress-ng --cpu 2 --timeout 180s

## Troubleshooting Workflow

Detect
   ↓
Investigate
   ↓
Identify Root Cause
   ↓
Fix
   ↓
Verify Recovery

## Result

Successfully implemented a monitoring and troubleshooting system for a
Dockerized application running on AWS EC2.