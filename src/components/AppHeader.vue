<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top"  style="background-color: #3E905C;">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">          
          <img alt="Camera Icon" class="logo" id="header_icon" src="@/assets/Lcamera_icon.png"/>
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
              <RouterLink class="nav-link" to="/myprofile">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/myprofile">Logout</RouterLink>
            </li>


          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
  import { RouterLink } from "vue-router";
</script>

<style>
 #header_icon{
  margin: 0px 2px 2px 0px;
  width: 23px;
  height: 23px;
 }
</style>