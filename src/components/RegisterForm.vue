<template>
    <div id="regis_formdiv">

        <div id="regis_headerdiv">
            <img alt="Camera Icon" id="regis_headerpic" src="@/assets/Dcamera_icon.png"/>
            <h3 id="regis_headertxt">Photogram</h3>              
        </div>

        <div id="regis_forminput">
            <form @submit.prevent="registerUser">          
                <div id="regis_forminfo">
                <p>
                    Connect with fellow wanderers, share your travel memories, and discover 
                    hidden gems. Sign up and let the globe unfold before your eyes. 
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

                <div class="form-group"> 
                <label>First Name</label>
                <input type="text" class="form-control" v-model="formData.fname" required><br>         
                </div>

                <div class="form-group"> 
                <label>Last Name</label>
                <input type="text" class="form-control" v-model="formData.lname" required><br>         
                </div>

                <div class="form-group">   
                <label>Email</label>
                <input type="email" class="form-control" v-model="formData.email" required><br>       
                </div>

                <div class="form-group">  
                <label>Location</label>
                <input type="text" class="form-control" v-model="formData.location"><br>        
                </div>

                <div class="form-group">  
                <label>Bio</label>
                <textarea class="form-control" v-model="formData.bio"></textarea><br>        
                </div>

                <div class="form-group">  
                <label>Photo</label>
                <input type="file" class="form-control" @change="handleFileUpload"><br>        
                </div>

                <div class="form-group" id="regis_formbtndiv"> 
                <button type="submit" class="btn" id="regis_formbtn">Register</button>         
                </div>
            </form>
        </div>

    </div>

    <p v-if="error">{{ error }}</p>
    <p v-if="success">{{ success }}</p>
</template>

<script setup>
    import { ref } from 'vue';
    import axios from 'axios';
    
    const formData = ref({
      username: '',
      password: '',
      fname: '',
      lname: '',
      email: '',
      location: '',
      bio: '',
      photo: null
    });
    const error = ref('');
    const success = ref('');
    
    const registerUser = async () => {
      try {
        const formDataObj = new FormData();
        for (const key in formData.value) {
          formDataObj.append(key, formData.value[key]);
        }
        const response = await axios.post('http://localhost:8080/api/v1/register', formDataObj, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        if (response.data.message === 'User created successfully') {
          success.value = response.data.message;
        } else {
          error.value = response.data.message;
        }
      } catch (error) {
        error.value = 'An error occurred while registering the user.';
      }
    };
    
    const handleFileUpload = (event) => {
      formData.value.photo = event.target.files[0];
    };
</script>

<style>
  #regis_formdiv{
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

  #regis_headerdiv{
    display: flex;
    justify-content: center;
    margin: 0px 0px 10px 0px;
  }

  #regis_headerpic{
    margin: 0px 7px 0px 0px;
    width: 32px;
    height: 32px;
  }

  #regis_headertxt{
    font-size: 25px;
  }

  div label, div input{
    font-size: 15px;
    font-weight: bold;
    color: rgb(55, 55, 55);
    display: block-inline;
  }
  
  #regis_forminput{
    display: flex;
    justify-content: center;
  }

  #regis_forminfo{
    display: flex;
    flex-direction: column;
    text-align: center;
    margin: 0px 0px 15px 0px;
    border: 0.4px solid rgb(179, 179, 179);
    border-radius: 4px;
    padding: 10px 10px 2px 10px;
  }

  #regis_formbtn{
    background-color: #3E905C;
    color: #fff;
    width: 100%;
  }

  #regis_formbtn:hover {
    background-color: #347d5c;
    cursor: pointer;
  }

  #regis_formbtndiv{
    display: flex;
    justify-content: center;
  }
</style>