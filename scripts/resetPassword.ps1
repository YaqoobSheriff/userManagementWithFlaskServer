param([String]$data)
$str=$data.split("-")
[System.Collections.ArrayList]$userp = $str
$userp.RemoveAt($str.Count-1)

ForEach($line in $userp)
     {
      $temp=$line.split(' ')
      $username=$temp[0]
      $password=$temp[1]
      try
        {
		    Set-ADAccountPassword -Identity $username -Reset -NewPassword (ConvertTo-SecureString -AsPlainText $password -Force)
		    Write-Host "Password changed successfully to user:$username."
	    }
	   catch 
	    {
        	Write-Host $Error[0].Exception.Message
	    }
	
}
