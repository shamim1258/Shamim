# AWS
-  Link to check all AWS Regions, Availability Zones and Data-Center Location https://infrastructure.aws/
-  AWS is divided in different regions.
-  AWS Region Compliance with data governance and legal requirements.
-  Region wise price also varies.
-  Region has many Availability Zones varies from min-2 to max-6.

**Links :**  
-  [Policy](policy.md)  
-  [Lambda](Lambda/base.md)  
-  [Creating EC2 Network](EC2.md)  

### Services
-  **Global :**
   -  IAM

### EC2
-  EC2, a Virtual Machine in the cloud on which you have OS-level control. You can run this cloud server whenever you want and can be used when you need to deploy your own servers in the cloud, similar to your on-premises servers, and when you want to have full control over the choice of hardware and the updates on the machine.
-  It mainly consists of :
   -  EC2 - Renting Virtual Machines
   -  [EBS](#ebs) - Stroing data in virtual drives
   -  ELB - Distributing load across machines
   -  [ASG](#asg) - Scaling the services using auto-scaling group
-  EC2 sizing & configuration options
   -  Operating System (OS): Linux, Windows or Mac OS
   -  How much compute power & cores (CPU)
   -  How much random-access memory (RAM)
   -  How much storage space:
      -  Network-attached ([EBS](#ebs) & EFS)
      -  hardware (EC2 Instance Store)
         -  One important thing to note here is the “delete on termination’ should be “Yes”. By default, it is enabled to yes, which means that once we terminate our EC2 instance, then this volume is also going to be deleted.
   -  Network card: speed of the card, Public IP address
   -  Firewall rules: [Security Group](#security-group)
   -  Bootstrap script (configure at first launch): EC2 User Data
-  Bootstraping or User Data - It is script or commands we specify which will run only once when the machine starts and it runs with root user.
-  [Security Group](#security-group) are acting as a “firewall” on EC2 instances


### Security Group
-  Security Groups are the fundamental of network security in AWS.
-  Security groups only contain **allow** rules.
-  Security groups rules can reference by IP or by security group.
-  They authorize access to - IP range, Port, Inbound and Outbound network.
-  If your application is not accessible (time out), then it’s a security group issue.
-  One Security Group can be linked with multiple instances.
-  One Security Group can contain another which is mentioned in IP field.

### AMI
-  AMI stands for Amazon Machine Image.
-  It is customization of EC2 with added configuration, software installed and etc.
-  It is created from EC2->template and Image and later using this we can create the instance same to this EC2 using this image.
-  When creating EC2 instance instead of selecting OS Names we can select AMI and create EC2 using this and Instance startup time is also fast as all program already installed in this new instace from image.

## Storage

### EBS
-  EBS stands for Elastic Block Store.
-  Network drive attached to your EC2 instance so it uses the network to communicate the instance.
-  Data exists even if instance in terminated.
-  Bound to a specific availability zone.
-  It can detached from one instace and attached to another instace in case when want to attach to instace in other availability zone than first take the snapshot of ebs and than create ebs in desired availability zone or region.
-  Can only be mounted to one instance at a time.
-  Analogy: Think of them as a “network USB stick”.
-  Free tier: 30 GB of free EBS storage of type General Purpose (SSD) or 
Magnetic per month.
-  One EBS can be attached to multiple EC2 instance and maximum limit it 16 EC2 instances.

### EBS Snapshot
-  It is backup(snapshot) of EBS volume at a point in time.
-  Not necessary to detach volume to do snapshot, but recommended.
-  Can copy snapshots across Availability Zones or Region

### EC2 Instance Store
-  It is high performance hardware disk.
-  EC2 Instance Store lose their storage if they’re stopped.
-  Backups and Replication are your responsibility.

### EFS
-  EFS stands for Elastic File System.
-  It is network file system can be mounted to many EC2 instances.
-  Highly available, scalabile and expensive.
-  It uses Security Group for access control.
-  Compatible with Linux based AMI (not windows).

## Other Concept

### Scalability
-  Scalability means that an application / system can handle greater loads by adapting.
-  Types :
   -  Vertical Scalability
      -  Vertically scalability means increasing the size of the instance.
      -  Example running application from t2.micro to t2.large.
      -  RDS, ElastiCache are services that can scale vertically. 
   -  Horizontal Scalability (also called elasticity)
      -  Horizontal Scalability means increasing the number of instances / systems.
      -  Horizontal scaling implies distributed systems.

### High Availability
-  High Availability usually goes hand in hand with horizontal scaling.
-  The goal of high availability is to survive a data center loss.

### Load Balancing
-  Load Balances are servers that forward traffic to multiple servers (EC2 instances) downstream grouped together into Target Group.
-  Target Group are group of EC2 intances which declared in Load Balancer.
-  Security Group created at Load Balancer side to handle the public user traffic which is than forwarded to EC2 client and these EC2 instance Security Group contains the Load Balancer Security Group which will automatically traffic from Load Balancer to EC2 instance.
-  EC2 Instance don't see the IP of client directly as traffic is coming from Load Balancer so this EC2 instance is receiving private traffic not public.
-  It benefits by getting single single point of access (DNS) to your applications connecting to more than one instances.
-  Load Balancing server regularly does regular health checks of downstream instances.
-  Enforce stickiness with cookies.
-  High availability across zones.
-  Separate public traffic from private traffic
-  AWS has 4 kinds of managed Load Balancers :
   -  Classic Load Balancer (CLB)
      -  Supports TCP (Layer 4), HTTP & HTTPS (Layer 7)
      -  HTTP, HTTPS, TCP, SSL (secure TCP)
   -  Application Load Balancer (ALB)
      -  Application load balancers is Layer 7 (HTTP)
      -  HTTP, HTTPS, WebSocket
      -  Load balancing to multiple HTTP applications across machines (target groups).
      -  Load balancing to multiple applications on the same machine (example containers).
      -  Routing tables to different target groups:
         -  Routing based on path in URL (example.com/users & example.com/posts)
         -  Routing based on hostname in URL (one.example.com & other.example.com)
         -  Routing based on Query String, Headers (example.com/users?id=123&order=false)
      -  ALB are a great fit for micro services & container-based application (example: Docker & Amazon ECS).
   -  Network Load Balancer NLB 
      -  TCP, TLS (secure TCP), UDP
      -  Network load balancers (Layer 4) allow to:
         -  Forward TCP & UDP traffic to your instances
         -  Handle millions of request per seconds.
         -  Less latency ~100 ms (vs 400 ms for ALB)
      -  NLB has one static IP per AZ, and supports assigning Elastic IP
      -  NLB are used for extreme performance, TCP or UDP traffic.
      -  NLB target group cab be group of 
         -  EC2 instance
         -  IP Address - private ips
         -  ALB
   -  Gateway Load Balancer – GWLB
      -  Operates at layer 3 (Network layer) – IP Protocol
      -  User traffic first reach to GWLB which will forward to network security applications target group than to EC2 instance destination application.
      -  Deploy, scale, and manage a fleet of 3rd party network virtual appliances in AWS.
      -  Example: Firewalls, Intrusion Detection and Prevention Systems, Deep Packet Inspection Systems, payload manipulation.
      -  GWLB target group cab be group of 
         -  EC2 instance
         -  IP Address - private ips

#### Elastic Load Balancer
-  An Elastic Load Balancer is a managed load balancer means it is managed by AWS.
-  It costs less to setup your own load balancer but it will be a lot more effort on your end.
-  It is integrated with many AWS offerings / services
   -  EC2, EC2 Auto Scaling Groups, Amazon ECS
   -  AWS Certificate Manager (ACM), CloudWatch
   -  Route 53, AWS WAF, AWS Global Accelerator

### Sticky Sessions
-  It is possible to implement stickiness so that the same client is always redirected to the same instance behind a load balancer.
-  This works for Classic Load Balancers and Application Load Balancers.
-  The “cookie” used for stickiness has an expiration date you control.
-  Sticky Session cookies :
   -  Application-based Cookies
      -  Custom cookie
         -  Generated by target
      -  Application cookie
         -  Generated by load balancer
   -  Duration-based Cookies
      -  Cookie generated by the load balancer

### Cross-Zone Load Balancing
-  Traffic is distributed evenly across all EC2 instances in all Availability Zones even if they are linked with different Load Balancers.
-  For ALB enabled by default (can be disabled at the Target Group level).
-  For NLB and GWLB it is disabled by default.

### ASG
-  ASG stands for Auto Scaling Group.
-  It is used to :
   -  Scale Out : Create new EC2 instances in case of increase of load.
   -  Scale In : Remove existing EC2 instances when load reduces.
   -  Automatically register new EC2 instances to load balancer.
   -  Recreate new EC2 instance in case previous one is terminated (example if unhealty).
   -  Ensure minimum and maximum number of instance are running.
-  While creating ASG you have provide all detail required to create EC2 instance and also Min size / Max Mize / Initial Capacity.
-  Scaling Policy : this is the criteria you set to Scale Out or Scale In example - Network traffic, Request count, CPU utilization and also on Cloudwatch alarm.
-  Auto Scaling Group which is dynamically scaling policy :
   -  Target Tracking Scale
      -  Most simple and easy to set-up.
      -  Example: I want the average ASG CPU to stay at around 40%
   -  Simple / Step Scaling
      -  When a CloudWatch alarm is triggered (example CPU > 70%), then add 2 units.
      -  When a CloudWatch alarm is triggered (example CPU < 30%), then remove 1.
   -  Scheduled Actions
      -  Anticipate a scaling based on known usage patterns.
      -  Example: increase the min capacity to 10 at 5 pm on Fridays
-  It is free service you only for EC2 instance.

### RDS
-  RDS stands for Relational Database Service.
-  It allows you to create databases in the cloud that are managed by AWS
-  Database allowed - Postgres, MySQL, MariaDB, Oracle, Aurora (AWS Database).
-  Advantages of RDS verses deploying DB on EC2 :
   -  Continuous backups and restore to specific timestamp (Point in Time Restore)
   -  Monitoring dashboards
   -  **Read replicas** for improved read performance (upto 5 read replicas).
      -  Replica can be created within AZ, cross AZ and cross Region.
      -  Replication is async so reads are eventually consistent.
   -  Multi AZ setup for DR (Disaster Recovery)
   -  **Auto Scaling** capability (vertical and horizontal) : When RDS detects you are running out of free database storage, it scales automatically.
   -  Storage backed by EBS (gp2 or io1)
-  Disadvantage :
   -  BUT you can’t SSH into your instances.

### ElastiCache
-  The same way RDS is to get managed Relational Databases.
-  ElastiCache is to get managed Redis or Memcached
-  Caches are in-memory databases with really high performance, low latency.
-  Using ElastiCache involves heavy application code changes.
-  Applications queries ElastiCache, if not available, get from RDS and store in ElastiCache.
-  Cache must have an invalidation strategy to make sure only the most current data is used in there.
-  Cache design patter :
   -  Lazy Loading / Cache Aside / Lazy Population
      -  Only requested data is cached.
      -  Cache miss penalty that results in 3 round trips.
   -  Write Through
      -  Add or Update cache when database is updated.
      -  Read are quick
      -  Write operation will be slow

### Route 53
-  DNA stand for Domain Name System which human readable format of hostname which is translated to ip address.
-  Route 53 is bascially used to register self owned hostname or using hostname or ip.
