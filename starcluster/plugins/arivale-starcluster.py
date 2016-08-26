from starcluster.clustersetup import ClusterSetup

class ClusterConfiguration(ClusterSetup):
     def __init__(self):
          pass
     def run(self, nodes, master, user, user_shell, volumes):
          for node in nodes:
    
               # Remove the master node from the queue
               master.ssh.execute('qconf -sq all.q | sed -e "s/\[master=.\]/\[master=0\]/" > /tmp/q.tmp && qconf -Mq /tmp/q.tmp')

               # Get latest version of analytics-notebook
               node.ssh.execute('sudo -H -u ubuntu bash -c "docker pull trueprint/analytics-notebook"')

               # Get latest github repositories
               node.ssh.execute('sudo -H -u sgeadmin bash -c "cd /home/sgeadmin/analytics && git pull"')
               node.ssh.execute('sudo -H -u sgeadmin bash -c "cd /home/sgeadmin/arivale_util && git pull"')
               node.ssh.execute('sudo -H -u sgeadmin bash -c "cd /home/sgeadmin/starcluster && git pull"')

               # Start docker instances on all worker nodes
               node.ssh.execute('docker run -d -v /home/sgeadmin/analytics:/pythonpath:ro -v /home/sgeadmin/starcluster:/scripts:ro -e "PYTHONPATH=/pythonpath" --name=analytics-notebook trueprint/analytics-notebook')
