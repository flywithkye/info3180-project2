<template>
<header>
  <nav class="navbar navbar-expand-lg navbar-dark fixed-top" style="background-color: #3E905C;">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">
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
            <RouterLink class="nav-link" :to="{ path: '/users', params: { userId } }">My Profile</RouterLink>
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
  const userId = ref(null)

  // Function to extract user ID from token
  function getUserIdFromToken() {
    try {
      // Get the token from local storage
      const token = localStorage.getItem('access_token');
      if (!token) {
        return null;
      }

      // Split the token by the delimiter (assuming a JWT structure)
      const payloadParts = token.split('.');
      if (payloadParts.length !== 3) {
        return null;
      }

      // Decode the payload from base64 to a string
      const decodedPayload = decodeURIComponent(atob(payloadParts[1]).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));

      // Parse the decoded payload
      const parsedPayload = JSON.parse(decodedPayload);

      // Extract the user id from the payload based on the provided structure
      return parsedPayload.sub;
    } catch (error) {
      console.error("Error extracting user id from token:", error);
      return null;
    }
  }

  // Get user ID from token
  userId.value = getUserIdFromToken();
</script>

<style>
 #header_icon{
  margin: 0px 2px 2px 7px;
  width: 23px;
  height: 23px;
 }
</style>