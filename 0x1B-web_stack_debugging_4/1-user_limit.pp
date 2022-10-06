# Changing the OS configuration
exec { 'hard':
  command => 'sed "/holberton hard/s/5/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft':
  command => 'sed "/holberton soft/s/4/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
