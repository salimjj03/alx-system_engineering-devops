# Kills a process 'killmenow' using Puppet

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
