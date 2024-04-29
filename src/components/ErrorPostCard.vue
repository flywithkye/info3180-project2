<script setup>
    import axios from 'axios';
    import { onMounted, ref } from 'vue';
    import { useRoute } from 'vue-router';

    const props = defineProps(['post']);
    console.log('User ID:', props.post.user_id);
    const userData = ref({});
    const likesCount = ref(null);
    const route = useRoute();

    async function getUserInfo() {
        try {
            const response = await axios.get(`http://localhost:8080/api/v1/users/${props.post.user_id}`);
            userData.value = response.data;
            console.log("Post Card User Data", userData.value);

        } catch (error) {
            console.log("This is error")
            console.error("Error:", error);
            // Handle error and display user-friendly message
        }
    }



  // Function to extract user ID from token
  function getUserIdFromToken() {
    try {
      // Get the token from local storage
      const token = localStorage.getItem('access_token');
      console.log('Token from local storage:', token);

      if (!token) {
        console.log('No token found in local storage.');
        return null;
      }

      // Split the token by the delimiter (assuming a JWT structure)
      const payloadParts = token.split('.');
      console.log('Payload parts:', payloadParts);

      if (payloadParts.length !== 3) {
        console.log('Invalid token format.');
        return null;
      }

      // Decode the payload from base64 to a string
      const decodedPayload = decodeURIComponent(atob(payloadParts[1]).split('').map(function(c) {
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




async function getLikesForPost() {
  try {
    const response = await axios.get(`http://localhost:8080/api/v1/posts/${props.post.id}/likes_count
`);
    likesCount.value = response.data.likes_count;

        console.log("Likes Count is", likesCount.value);

    } catch (error) {
        console.log("This is error")
        console.error("Error:", error);
        // Handle error and display user-friendly message
    }
    }



const loggedInUser = getUserIdFromToken()
async function likePost() {
  try {
    const config = {
      headers: {
        'user-id': loggedInUser
      }
    };
  }
}
    
</script>


<template>
    <div class="post">
        <div id="userdiv">
            <div id="userdivinner1">
                <!-- <img id="userphoto" alt="..." src="@/assets/nature_pic.jpg"> -->
                <img
                    alt="User Profile Picture"
                    id="userphoto"
                    :src="'../uploads/' + userData.profile_photo" 
                />
                <p id="username"> <router-link class="nav-link" :to="{ name: 'users', params: { id: post.user_id } }">{{ userData.username }}</router-link> </p>
            </div>
                
            <div id="userdivinner2">
                <p id="postdate">{{ post.created_on }}</p>
            </div>
        </div>

        <div id="postinfo">
            <div id="postphotodiv">
                <img id="postphoto" :src="'../uploads/' + post.photo" alt="Post photo">
            </div>
            <p id="postcaption">{{ post.caption }}</p>

            <div id="postdetails">
                <div id="postlikesdiv">
                    <img @click="likePost" alt="Likes Icon" id="postlikesicon" src="@/assets/likes_icon.png"/>
                    <p id="postlikes">{{likesCount}} Likes</p>
                    <!-- <p v-else id="postlikes">0 Likes</p> -->

                    <!-- meant to be like this: <p id="postlikes">{{ post.likes }} Likes</p> -->
                </div>
                
                <div id="postsharediv">
                    <img alt="Share Icon" id="postshareicon" src="@/assets/share_icon.png"/>
                    <p id="postshare">Share</p>
                </div>
            </div>                            
            
        </div>     
    </div>
</template>
  
<style scoped>
    /* Add any component specific styles here */
    .post {    
        background: rgba(255, 255, 255, 0.817);
        border: 0.5px solid #b9babb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-radius: 6px 6px 6px 6px;
        min-width: 600px;     
        max-width: 800px;
        position: relative;
        margin: auto;
        /*margin-left: 50px;*/
    }

    #userdiv{
        display: flex;    
        justify-content: space-between;
        padding: 15px 20px 13px 15px;
        color: #3f3e3e;
    }

    #userdivinner1{
        display: flex;
    }
    
    #userphoto {
        width: 25px;
        height: 25px;
        object-fit: cover;
        border-radius: 50px;
        margin: 0px 10px 0px 0px;
    }

    #username{        
        cursor: pointer;
    }
    #username:hover {
        text-decoration: underline;
    }

    #postinfo {
        margin-top: -15px;
    }

    #postphotodiv {
        margin: 0;
        height: 370px;
    }

    #postphoto {
        width: 100%;
        height: 370px;
        object-fit: cover;
    }

    #postcaption{
        padding: 10px 21px 10px 21px;
    }

    #postdetails{    
        display: flex;    
        justify-content: space-between;
        padding: 10px 20px 10px 20px;
        color: #3f3e3e;
    }

    #postlikesdiv{
        display: flex;        
        cursor: pointer;
    }
    #postlikesdiv:hover #postlikes{
        color: #b13131;
    }
    #postlikes{
        font-weight: bold;
    }
    #postlikesicon{        
        margin: 0px 4px 15px 0px;
        width: 25px;
        height: 25px;
    }
    

    #postsharediv{
        display: flex;       
        cursor: pointer;
    }
    #postsharediv:hover #postshare{
        color: #347d5c;
    }
    #postshare{
        font-weight: bold;
    }
    #postshareicon{        
        margin: 0px 9px 15px 0px;
        width: 25px;
        height: 25px;
    }


</style>