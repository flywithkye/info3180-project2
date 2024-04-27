<template>
    <div id="displayFeedback">
      <div id="loginError" v-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
      <div id="loginSuccess" v-if="success" class="alert alert-success" role="alert">{{ success }}</div>
    </div>
    
    <div id="login_formdiv">
        <div id="login_headerdiv">
            <img alt="Camera Icon" id="login_headerpic" src="@/assets/Dcamera_icon.png"/>
            <h3 id="login_headertxt">Photogram</h3>              
        </div>

        <div id="login_forminput">
            <form @submit.prevent="loginUser">          
                <div id="login_forminfo">
                <p>
                  Welcome Back! Ready to return to the world of Photogram? Login now.
                </p>
                </div>

                <div class="form-group">
                <label>Username</label>
                <input type="text" class="form-control" v-model="formData.username" required><br>
                </div>

                <div class="form-group">   
                <label>Password</label>
                <input type="password" class="form-control" v-model="formData.password" required><br>       
                </div>

                <div class="form-group" id="login_formbtndiv"> 
                <button type="submit" class="btn" id="login_formbtn">Login</button>         
                </div>
            </form>
        </div>

    </div>

</template>

<script setup>
    import { ref } from 'vue';
    import axios from 'axios';
    
    const formData = ref({
      username: '',
      password: ''
    });
    const error = ref('');
    const success = ref('');
    
    const loginUser = async () => {
        try {

          const formDataObj = new FormData();
        for (const key in formData.value) {
          formDataObj.append(key, formData.value[key]);
        }

            const response = await axios.post('http://localhost:8080/api/v1/auth/login', formDataObj, {
              headers: {
            'Content-Type': 'form-data'
          }
            });

            // Check if login was successful
            if (response.status === 200) {
                success.value = response.data.message;
                console.log(response.data.access_token)
                localStorage.setItem('access_token', response.data.access_token);

                // Redirect or perform any other action after successful login
            } else {
                error.value = 'Invalid username or password';
            }
        } catch (error) {
            console.error(error);
            error.value = 'An error occurred while logging in the user.';
        }
    };
    
</script>

<style>  
  #displayFeedback{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  #login_formdiv{
    display: flex;
    flex-direction: column;
    min-width: 100px;
    max-width: 500px;
    margin: 30px auto auto auto;
    border: 0.4px solid rgb(179, 179, 179);
    box-shadow: rgba(17, 17, 26, 0.1) 0px 0px 16px;
    border-radius: 4px;
    padding: 40px;
  }

  #login_headerdiv{
    display: flex;
    justify-content: center;
    margin: 0px 0px 10px 0px;
  }

  #login_headerpic{
    margin: 0px 7px 0px 0px;
    width: 32px;
    height: 32px;
  }

  #login_headertxt{
    font-size: 25px;
  }

  div label, div input{
    font-size: 15px;
    color: rgb(55, 55, 55);
    display: block-inline;
  }
  
  #login_forminput{
    display: flex;
    justify-content: center;
  }

  #login_forminfo{
    display: flex;
    flex-direction: column;
    text-align: center;
    margin: 0px 0px 15px 0px;
    border: 0.4px solid rgb(179, 179, 179);
    border-radius: 4px;
    padding: 10px 10px 2px 10px;
  }

  #login_formbtn{
    background-color: #3E905C;
    color: #fff;
    width: 100%;
  }

  #login_formbtn:hover {
    background-color: #347d5c;
    cursor: pointer;
  }

  #login_formbtndiv{
    display: flex;
    justify-content: center;
  }
</style>