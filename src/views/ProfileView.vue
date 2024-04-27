<template>
  <div class="container">
    <div id="profilepg-div">
      <div id="userinfopg">
        <div class="box" id="user-info-pic">
          <!-- <img
            alt="User Profile Picture"
            id="user-photo"
            :src="userData.value?.avatar || '/default-profile.png'" 
          /> -->
        </div>
        <div id="user-info" class="box">
          <h4 id="user-name">{{ userData.firstname }} {{ userData.value?.lastname }}</h4>
          <p id="user-location">{{ userData.value?.location }}</p>
          <p id="user-joined">Member since: January, 2018</p>
          <p id="user-bio">{{ userData.value?.bio }}</p>
        </div>
        <div id="user-stats" class="box">
          <div id="followers">
            <span id="user-follow-num">{{ userData.value?.followers?.length || 0 }}</span>
            <span id="user-followers">Followers</span>
          </div>
          <div id="posts">
            <span id="user-posts-num">{{ userData.value?.posts?.length || 0 }}</span>
            <span id="user-posts">Posts</span>
          </div>
          <div id="user-buttondiv">
            <button id="user-button">Follow</button>
          </div>
        </div>
      </div>
      <div id="contentpg">
        <div v-for="post in userData.value?.posts || []" :key="post.id">
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

const userData = ref(null);
const route = useRoute();

async function getUserInfo() {
  try {
    const response = await axios.get(`http://localhost:8080/api/v1/users/1`);
    userData.value = response.data;
    console.log("Profile view user data");
  } catch (error) {
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
    grid-template-columns: 33% 33% 33%;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    width: 70vw;
    height: 30vh;
    border-radius: 20px;
  }
  
  #profilepg-div{
    display: grid;
    gap: 0px 10px;
    grid-template-rows: minmax(0, 1fr) auto; 
    padding: 35px 20px 20px 20px;
  }

  #contentpg{
    display: grid;
    grid-template-columns: auto auto auto;
    padding: 2%;
  }

  #image-div{
    border: solid;
    width: 35%;
  }

  #image{
    width: 100%;
    padding: 5%;
  }

  #user-photo{
    padding: 5%;
    border-radius: 100%;
    width: 20vw;
    height: 30vh;
  }

  #user-info{
    text-align: left;
  }

  #user-name{
    padding-top: 5%;
  }

  #user-stats{
    padding: auto;
  }

  #user-location{
    padding-top: 10%;
  }

  #user-joined{
    padding-bottom: 5%;
  }

  #user-stats{
    display: grid;
    grid-template-areas: 
    'posts posts followers followers'
    'button button button button';
  }

  #user-buttondiv{
    grid-area: button;
  }

  #user-button{
    padding: 2% 30% 2% 30%;
    background-color: yellowgreen;
  }

  #followers{
    display: grid;
    grid-template-rows: auto auto;
    grid-area: followers;
  }

  #posts{
    display: grid;
    grid-template-rows: auto auto;
    grid-area: posts;
  }

  



</style>