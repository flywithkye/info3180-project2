<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="registerUser">
        <label>Username:</label>
        <input type="text" v-model="formData.username" required><br>
        <label>Password:</label>
        <input type="password" v-model="formData.password" required><br>
        <label>First Name:</label>
        <input type="text" v-model="formData.fname" required><br>
        <label>Last Name:</label>
        <input type="text" v-model="formData.lname" required><br>
        <label>Email:</label>
        <input type="email" v-model="formData.email" required><br>
        <label>Location:</label>
        <input type="text" v-model="formData.location"><br>
        <label>Bio:</label>
        <textarea v-model="formData.bio"></textarea><br>
        <label>Photo:</label>
        <input type="file" @change="handleFileUpload"><br>
        <button type="submit">Register</button>
      </form>
      <p v-if="error">{{ error }}</p>
      <p v-if="success">{{ success }}</p>
    </div>
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
      const response = await axios.post('http://192.168.0.2:8080/register', formDataObj, {
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
    