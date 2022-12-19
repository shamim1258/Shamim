# AWS overview :

-  Link to check all AWS Regions, Availability Zones and Data-Center Location https://infrastructure.aws/
-  AWS is divided in different regions.
-  AWS Region Compliance with data governance and legal requirements.
-  Region wise price also varies.
-  Region has many Availability Zones varies from min-2 to max-6.

**Services :**
-  **Global :**
   -  **IAM**

**EC2 :**
-  EC2, a Virtual Machine in the cloud on which you have OS-level control. You can run this cloud server whenever you want and can be used when you need to deploy your own servers in the cloud, similar to your on-premises servers, and when you want to have full control over the choice of hardware and the updates on the machine.
-  It mainly consists of :
   -  EC2 - Renting Virtual Machines
   -  [EBS](#ebs) - Stroing data in virtual drives
   -  ELB - Distributing load across machines
   -  ASG - Scaling the services using auto-scaling group
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

**Links :**  
-  [Policy](policy.md)  
-  [Lambda](Lambda/base.md)  
-  [Creating EC2 Network](EC2.md)  

### Security Group
-  Security Groups are the fundamental of network security in AWS.
-  Security groups only contain **allow** rules.
-  Security groups rules can reference by IP or by security group.
-  They authorize access to - IP range, Port, Inbound and Outbound network.
-  If your application is not accessible (time out), then it’s a security group issue.

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

### EBS Snapshot
-  It is backup(snapshot) of EBS volume at a point in time.
-  Not necessary to detach volume to do snapshot, but recommended.
-  Can copy snapshots across Availability Zones or Region
