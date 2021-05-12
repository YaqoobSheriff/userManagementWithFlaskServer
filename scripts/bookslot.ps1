param([String]$data)

$str=$data.split("*")
[System.Collections.ArrayList]$users = $str
$users.RemoveAt($str.Count-1)

foreach($user in $users)
{
 $details=$user.split(' ')
 $username=$details[0]
 $bookingDay=$details[1]
 $bookingTime=$details[2]

$day=$bookingDay

$time=$bookingTime
$bookTime=$time.replace(":30",":00")
$user=$username
$slotTimeindex=$bookTime.IndexOf("-")
$bookFrom=$bookTime.substring(0,$slotTimeindex)
$bookfrom1=$bookFrom.Replace(":00",":30")
$bookTo=$bookTime.substring($slotTimeindex+1)
$bookTo1=$bookTo.Replace(":00",":30")
$lowerCase=$day.ToLower()

try{
    $u=Get-ADUser -Identity $user
   
    if($u){
        $bookStatus=net user $user /time:$day,$bookTime
        Write-Host $user $bookStatus
        }
    }
    Catch{
    $Error[0].Exception.Message
    }
 }


