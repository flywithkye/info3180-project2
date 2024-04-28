<template>
<header>
  <nav class="navbar navbar-expand-lg navbar-dark fixed-top" style="background-color: #3E905C;">
    <div class="container-fluid">
      <a class="navbar-brand" href="/explore">
        <img alt="Camera Icon" class="logo" id="header_icon" src="@/assets/Lcamera_icon.png" />
        Photogram</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav navbar-right">
          <li class="nav-item">
            <RouterLink to="/" class="nav-link active">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/posts/new">Make Post</RouterLink>
          </li>
          <li class="nav-item">
            <!-- <RouterLink class="nav-link" :to="{ name: 'users', params: { id: userId } }">My Profile</RouterLink> -->
            <router-link class="nav-link" :to="{ name: 'users', params: { id: userId } }"> My Profile</router-link>
            
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/login">Login</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="">Logout</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</header>
</template>

<script setup>
  import { RouterLink } from "vue-router";
  import { ref, onMounted } from "vue";

  const userId = ref(null);

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

  // Initialize userId ref with user ID from token after component is mounted
  onMounted(() => {
    userId.value = getUserIdFromToken();
  });
</script>

<style>
 #header_icon{
  margin: 0px 2px 2px 7px;
  width: 23px;
  height: 23px;
 }
</style>