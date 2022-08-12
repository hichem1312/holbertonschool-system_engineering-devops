#create a manifest that kills a process
exec {'kill-killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin';
}
