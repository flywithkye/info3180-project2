<template>
  <div id="displayFeedback">
    <div id="loginError" v-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
    <div id="loginSuccess" v-if="success" class="alert alert-success" role="alert">{{ success }}</div>
  </div>
  <div id="create_formdiv">
    <div id="create_headerdiv">
      <h3 id="login_headertxt">Create Post</h3>
    </div>

    <div id="create_forminput">
      <form @submit.prevent="createPost">
        <div id="create_forminfo">
          <p>
            Share Your Adventures: Create a post and share your photos with the world.
          </p>
        </div>

        <div class="form-group">
          <label>Photo</label>
          <input type="file" class="form-control" @change="handleFileUpload"><br>
        </div>

        <div class="form-group">
          <label>Caption</label>
          <textarea class="form-control" v-model="formData.caption"></textarea><br>
        </div>

        <div class="form-group" id="create_formbtndiv">
          <button :disabled='!loggedIn' type="submit" class="btn" id="create_formbtn">Create Post</button>
        </div>
      </form>
    </div>

  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';

const formData = ref({
  caption: '',
  // userid: '',
  photo: null
});

var userId = ""
const error = ref('');
const success = ref('');
let loggedIn = false;

userId = getUserIdFromToken()
console.log("Postfrom User Id", userId)


// Function to extract user ID from token
function getUserIdFromToken() {
  try {
    // Get the token from local storage
    const token = localStorage.getItem('access_token');
    console.log('Token from local storage:', token);

    if (!token) {
      console.log('No token found in local storage.');
      error.value = "You must be logged in to create posts.";               
      loggedIn = false;
      return null;
    } else {  
      loggedIn = true;
    }

    // Split the token by the delimiter (assuming a JWT structure)
    const payloadParts = token.split('.');
    console.log('Payload parts:', payloadParts);

    if (payloadParts.length !== 3) {
      console.log('Invalid token format.');
      return null;
    }

    // Decode the payload from base64 to a string
    const decodedPayload = decodeURIComponent(atob(payloadParts[1]).split('').map(function (c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    console.log('Decoded payload:', decodedPayload);

    // Parse the decoded payload
    const parsedPayload = JSON.parse(decodedPayload);
    console.log('Parsed payload:', parsedPayload);

    // Extract the user id from the payload based on the provided structure
    const userId = parsedPayload.sub;
    console.log('Extracted user ID:', userId);

    return userId;
  } catch (error) {
    console.error("Error extracting user id from token:", error);
    return null;
  }
}


const createPost = async () => {

  try {
    const formDataObj = new FormData();
    for (const key in formData.value) {
      formDataObj.append(key, formData.value[key]);
    }
    const response = await axios.post(`http://localhost:8080/api/v1/users/${userId}/posts`, formDataObj, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    if (response.data.message === 'the post created successfully') {
      success.value = response.data.message;
    } else {
      error.value = response.data.message;
    }
  } catch (error) {
    error.value = 'An error occurred while uploaading the post.';
  }


};




const handleFileUpload = (event) => {
  formData.value.photo = event.target.files[0];
};

onMounted(() => {
  getUserIdFromToken();
});
</script>

<style>
#displayFeedback {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  z-index: 2;
  position: fixed;
  top: 70px;
  left: 0; 
  right: 0; 
  margin-left: auto; 
  margin-right: auto; 
}

#create_formdiv {
  display: flex;
  flex-direction: column;
  min-width: 100px;
  max-width: 500px;
  margin: 30px auto auto auto;
  border: 0.4px solid rgb(179, 179, 179);
  box-shadow: rgba(17, 17, 26, 0.1) 0px 0px 16px;
  border-radius: 4px;
  padding: 40px;
  background: rgba(255, 255, 255, 0.817);
}

#create_headerdiv {
  display: flex;
  justify-content: center;
  margin: 0px 0px 10px 0px;
}

#create_headerpic {
  margin: 0px 7px 0px 0px;
  width: 32px;
  height: 32px;
}

#create_headertxt {
  font-size: 23px;
}

div label,
div input {
  font-size: 16px;
  color: rgb(55, 55, 55);
  display: block-inline;
}

#create_forminput {
  display: flex;
  justify-content: center;
}

#create_forminfo {
  font-size: 20px;
  display: flex;
  flex-direction: column;
  text-align: center;
  margin: 0px 0px 15px 0px;
  border-radius: 4px;
  padding: 5px 10px 2px 10px;
  background: rgba(255, 255, 255, 0.228);
}

#create_formbtn {
  background-color: #3E905C;
  color: #fff;
  width: 100%;
}

#create_formbtn:hover {
  background-color: #347d5c;
  cursor: pointer;
}

#create_formbtndiv {
  display: flex;
  justify-content: center;
}
</style>