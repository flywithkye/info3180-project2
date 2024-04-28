<template>
  <div class="container">
    <div id="profilepg-div">
      <div id="userinfopg">
        <div class="box" id="user-info-pic">
        <img
            alt="User Profile Picture"
            id="user-photo"
            :src="userData.profile_photo || '../uploads/house1.jpg'" 
          />
        </div>
        <div id="user-info" class="box">
          <h4 id="user-name">{{ userData.firstname }} {{ userData.lastname }}</h4>
          <p id="user-location">{{ userData.location }}</p>
          <p id="user-joined">Member since: January, 2018</p>
          <p id="user-bio">{{ userData.bio }}</p>
        </div>
        <div id="user-stats" class="box">
          <div id="user-stats-inner">
            <div id="followers">
              <span id="user-follow-num">{{ userData.value?.followers?.length || 0 }}</span>
              <span id="user-followers">Followers</span>
            </div>
            <div id="posts">
              <span id="user-posts-num">{{ userData.value?.posts?.length || 0 }}</span>
              <span id="user-posts">Posts</span>
            </div>
          </div>
          <div id="user-buttondiv">
            <button id="user-button">Follow</button>
          </div>
        </div>
      </div>
      <div id="contentpg">
        <div v-for="post in userData.value?.posts || []" :key="post.id" id="post-card">
          <img :src="post.imageUrl" alt="User Post" />
          <p>{{ post.caption }}</p>
          </div>
        <p v-if="!userData.value?.posts?.length">No posts yet.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const userData = ref({});
const route = useRoute();

async function getUserInfo() {
  try {
    const response = await axios.get(`http://localhost:8080/api/v1/users/${route.params.id}`);
    userData.value = response.data;
    console.log("Profile view user data", userData.value);

  } catch (error) {
    console.log("This is error")
    console.error("Error:", error);
    // Handle error and display user-friendly message
  }
}

onMounted(() => {
  getUserInfo();
});


</script>



<style>
  #userinfopg{
    display: grid;
    grid-template-columns: minmax(28%, 28%) minmax(40%, 40%) minmax(30%, 30%);
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    width: 100%;
    min-height: 25vh;
    border-radius: 10px;
    margin-bottom: 3%;
  }
  
  #profilepg-div{
    display: grid;
    gap: 0px 10px;
    grid-template-rows: minmax(0, 1fr) auto; 
    padding: 35px 20px 20px 20px;
  }

  #contentpg{
    display: grid;
    gap: 30px 20px;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr);
    padding: 3%;
    border: 0.6px solid #b6b5b5;
    width: 100%;
    border-radius: 10px;
  }
 
  .post-image{
    object-fit: cover;
    height: 230px;
    width: 100%;
  }

  #post-card{
    border: 0.5px solid #ccc;
  }

  #user-photo{
    border-radius: 100%;
    object-fit: cover;
    height: 25vh;
    width: 15vw;
  }
  
  #user-info-pic{
    padding: 5%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #user-info{
    text-align: left;
  }

  #user-name{
    padding-top: 3%;
  }

  #user-location{
    padding-top: 3%;
  }

  #user-joined{
    margin-top: -15px;
    padding-bottom: 1%;
  }

  #user-stats{
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-right: 2%;  
  }

  #user-stats-inner{
    /*background-color: #d53232;*/
    display: flex;
    justify-content: space-evenly;
  }

  #user-buttondiv{
    display: flex;
    justify-content: center;   
    padding: 0% 0 0% 0;
  }

  #user-button{
    width: 100%;
    padding-top: 2%;
    padding-bottom: 2%;
    background-color: #3E905C;
    min-height: 30%;
    color: white;
  }

  #user-followers-name{
    width: 100%;
    text-align: center;
    padding: 1% 1% 0.5% 1%;
  }

  #user-posts-name{
    width: 100%;
    text-align: center;
    padding: 1% 1% 0.5% 1%;
  }


  #user-follow-num{
    font-weight: bold;
    margin-top: 10%;
    margin-bottom: -3px;
  }

  #user-posts-num{
    font-weight: bold;
    margin-top: 10%;
    margin-bottom: -3px;
  }

  



</style>