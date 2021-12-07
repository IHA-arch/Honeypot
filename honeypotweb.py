def fake_ftp_page_html():
    webpage = b'''
<!DOCTYPE html>   
<html>   
<head>  
<meta name="viewport" content="width=device-width, initial-scale=1">  
<title> FTP::Login::192.168.43.1 </title>  
<style>   
Body {  
  font-family: Calibri, Helvetica, sans-serif;  
  background-color: black;  
}  
button {   
       background-color: transparent;   
       width: 10%; 
       font-size: 30px;
        color: white;   
        padding: 10px;   
        margin: 10px 0px;   
        border: none;   
        cursor: pointer;   
         }   
 form {   
        border: 3px solid transparent;   
    } 
 input[type=text], input[type=password] {   
        width: 100%;   
        margin: 8px 0;  
        padding: 12px 20px;   
        display: inline-block;   
        border: 1px solid gray;   
        box-sizing: border-box;   
    }  
 h1 {
	 color: white;
 }
 address {
	 color:white;
 }
 button:hover {   
        opacity: 0.7;   
    }   
  .cancelbtn {   
        width: auto;   
        padding: 10px 18px;  
        margin: 10px 5px;  
    }   
        
     
 .container {   
        padding: 25px;   
        background-color: transparent;  
    }   
 .container label {
	 color: white;
 }
</style>   
</head>    
<body>    
    <center> <h1> FTP server </h1> </center>   
    <form>  
        <div class="container">   
            <label>Username  </label>   
            <input type="text" placeholder="Enter Username" name="username" required>  
            <label>Password  </label>   
            <input type="password" placeholder="Enter Password" name="password" required>  
            <button type="submit">Login</button>             
        </div>   
    </form> 
    <address>FTP Server</address>
</body>     
</html> 
        '''
    return webpage


