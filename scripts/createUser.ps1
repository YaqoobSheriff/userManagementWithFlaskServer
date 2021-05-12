param([String]$data)

$str=$data.split("-")
[System.Collections.ArrayList]$users = $str
$users.RemoveAt($str.Count-1)

function add-upn {
 Param ($upn)
   $upns=Get-ADForest|select UPNSuffixes
   $upnsuffixes=$upns.UPNSuffixes
        if($upnsuffixes -notcontains $upn)
            { 
            $upn
	        $upnMsg="The UPN doesn't exist hence adding UPN:$upn"
            Get-ADForest | Set-ADForest -UPNSuffixes @{Add=$upn}
	        $upnMsg="Added $upn"
            }
            return $upnMsg
}

foreach($line in $users)
     {
      $temp=$line.split(' ')
      $user=$temp[0]
      $password=$temp[1]
      $upn=$temp[2]
      add-upn -upn $upn
      #Change the path to your desired location
      $path= "CN=Users"+","+"DC=test"+","+"DC=com"
      $userpname = $user+"@"+$upn
      try{
         $output=New-ADUser -SamAccountName $_.SamAccountName -UserPrincipalName $userpname -Name $user -DisplayName $user -GivenName $user -SurName " " -Path $path -AccountPassword (ConvertTo-SecureString -AsPlainText $password -Force) -Enabled $True -PasswordNeverExpires $True -PassThru 
         write-host "$user created successfully"
         }
         catch{
            $m=$Error[0].Exception.Message
            Write-Host "$user $m"
         }
}




     

