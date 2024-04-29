<script setup>
    import axios from 'axios';
    import { onMounted, ref } from 'vue';
    import { useRoute } from 'vue-router';
    import ProfileViewPostCard from "@/components/ProfileViewPostCard.vue"

    const userData = ref({});
    const userPosts = ref({});
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

    async function getUserPosts() {
    try {
        const response = await axios.get(`http://localhost:8080/api/v1/users/${route.params.id}/posts`);
        userPosts.value = response.data;
        console.log("Profile view user posts", userPosts.value);
        console.log(Object.keys(userPosts.value).length);

    } catch (error) {
        console.log("This is error")
        console.error("Error:", error);
        // Handle error and display user-friendly message
    }
    }

    function isObjectEmpty(objectName) {
        return Object.keys(objectName).length === 0;
    }

    onMounted(() => {
        getUserInfo();
        getUserPosts();
    });
</script>


<template>
    <div id="profilepg-div">
      <div id="userinfopg">
        <div id="user-info-pic">
          <img
            alt="User Profile Picture"
            id="user-photo"
            :src="'../uploads/' + userData.profile_photo" />
        </div>
        <div id="user-info">
          <h1 id="user-name">{{ userData.firstname }} {{ userData.lastname }}</h1>
          <p id="user-location">{{ userData.location }}</p>
          <p id="user-joined">Member since {{userData.joined_on}}</p>
          <p id="user-bio">{{ userData.bio }}</p>
        </div>
        <div id="user-stats">
          <div id="user-stats-inner">
            <div id="user-followers-div">
              <p id="user-follow-num">{{ userData.value?.followers?.length || 0 }}</p>
              <p id="user-followers-name">Followers</p>
            </div>
            <div id="user-posts-div">
              <p id="user-posts-num">{{ userData.value?.posts?.length || 0 }}</p>
              <p id="user-posts-name">Posts</p>
            </div>
          </div>
          <div id="user-buttondiv">
            <button id="user-button" type="button" class="btn">Follow</button>
          </div>
        </div>
      </div>
      <div id="contentpg">
        <div id="posts"  v-if="!isObjectEmpty(userPosts)">
          <ProfileViewPostCard :post="post" v-for="post in userPosts" :key="post.id" />
        </div>
        <div id="postnotif" v-else>
          <p>No posts from {{ userData.firstname }} yet.</p>
        </div>
      </div>
    </div>
</template>


<style scoped>
  #userinfopg{
    display: grid;
    grid-template-columns: minmax(0, 210px) minmax(0, 650px) minmax(0, 250px);
    background: rgba(255, 255, 255, 0.817);
    width: 100%;
    min-height: 29vh;
    margin-bottom: 3%;
    border: 0.5px solid #b9babb;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    border-radius: 6px 6px 6px 6px;
    padding: 10px 20px 10px 20px;
  }
  
  #profilepg-div{
    display: grid;
    gap: 0px 10px;
    grid-template-rows: minmax(0, 1fr) auto; 
    padding: 35px 20px 20px 20px;
  }

  #user-photo{
    border-radius: 100%;
    object-fit: cover;
    height: 175px;
    width: 95%;
  }
  
  #user-info-pic{
    padding: 5px 10% 5px 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #user-info{
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: left;
  }

  #user-name{
    padding-top: 3%;
    font-weight: bold;
    font-size: 21px;
    color: #3F3E3E;
  }

  #user-location{
    padding-top: 1%;
    color: #3F3E3E;
  }

  #user-joined{
    margin-top: -15px;
    margin-bottom: 0px;
    color: #3F3E3E;
  }

  #user-bio{
    margin-top: 6px;
    color: #3F3E3E;
  }


  #user-stats{
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-right: 2%; 
    font-size: 18px; 
    padding: 5px 5px 5px 5px;
  }

  #user-stats-inner{
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

  #user-button:hover {
    background-color: #347d5c;
    cursor: pointer;
  }

  #user-followers-div {
    font-weight: bold;
    color: #3F3E3E;
  }
  #user-posts-div{
    font-weight: bold;
    color: #3F3E3E;
  }

  #user-followers-name{
    width: 100%;
    text-align: center;
    padding: 1% 1% 0.5% 1%;
    font-weight: normal;
  }

  #user-follow-num{
    margin-top: 15px;
    text-align: center;
    margin-bottom: -3px;
  }

  #user-posts-name{
    width: 100%;
    text-align: center;
    padding: 1% 1% 0.5% 1%;
    font-weight: normal;
  }

  #user-posts-num{
    margin-top: 15px;
    text-align: center;
    margin-bottom: -3px;
    color: #3F3E3E;
  }


  #contentpg{
    width: 100%;
    border-radius: 3px;
    padding: 25px 25px 25px 25px;
    margin-top: 5px;
    background: rgba(255, 255, 255, 0.817);
    border: 0.5px solid #b9babb;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }

  #posts {
    display: grid;
    gap: 33px 21px;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr);  
  }

  #postnotif {
    text-align: center;
    margin-bottom: -10px;
  }

</style>