param([String]$data)
$str=$data.split("*")
[System.Collections.ArrayList]$users = $str
$users.RemoveAt($str.Count-1)
foreach($user in $users)
{
  $details=$user.split(' ')
  $username=$details[0]
if ($username -like '*@wilp*') {
$splitUserName=$username.split("@")
$username=$splitUserName[0]
$username 
 }
 
[byte[]]$hours = @(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
try{
    $u=Get-ADUser -Identity $user
   
    if($u){
        get-ADUser -Identity $user | Set-ADUser -Replace @{Logonhours = [Byte[]]$hours}
        write-host "slots removed for user $user"
        }
    }
    Catch{
    $Error[0].Exception.Message
    }


}