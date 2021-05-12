param([String]$data)
$str=$data.split("-")
[System.Collections.ArrayList]$userp = $str
$userp.RemoveAt($str.Count-1)

ForEach($user in $userp)
     {
     try
     {
        Remove-ADUser -Identity $user -Confirm:$false
        Write-Host "$user deleted successfully"
     }
     catch 
	 {
       	Write-Host $Error[0].Exception.Message
	 }
	
}