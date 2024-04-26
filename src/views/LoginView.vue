<template>
  <div class="sign-in-container">
    <div class="row justify-content-center align-items-center vh-100">
      <div class="col-md-4">
        <div class="card shadow">
          <div class="card-body">
            <h1 class="card-title text-center mb-4">Sign In</h1>
            <form @submit.prevent="login">
              <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input v-model="username" type="text" id="username" name="username" class="form-control" required>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input v-model="password" type="password" id="password" name="password" class="form-control" required>
              </div>
              <div class="mb-3">
                <button type="submit" class="btn btn-primary btn-block">Login</button>
              </div>
              <div class="mb-3 text-center">
                <!-- <a href="#" class="text-muted">Forgot Password?</a> -->
              </div>
              <div class="mb-3 text-center">
                <p>Don't have an account? <router-link to="/signup">Sign Up</router-link></p>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'; // Importing ref for reactive variables

export default {
  setup() {
    // Reactive variables for username, password, flash message, and whether to display the flash message
    const username = ref('');
    const password = ref('');
    const flashMessage = ref('');
    const displayFlash = ref(false);
    const isSuccess = ref(false);

    // Function to handle login
    const login = async () => {
      // Basic validation
      if (!username.value || !password.value) {
        displayFlashMessage(false, 'Please enter both username and password.');
        return;
      }

      try {
        // Making a POST request to the Flask API login endpoint
        const response = await fetch('http://192.168.0.2:8080/api/v1/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: username.value,
            password: password.value,
          }),
        });

        const responseData = await response.json();

        if (response.ok) {
          // Assuming your Flask API returns a success message or token upon successful login
          if (responseData.success) {
            displayFlashMessage(true, 'Login successful.');
            // Redirect the user to another route upon successful login
            // Use router.push('/dashboard') if you're using Vue Router
          } else {
            displayFlashMessage(false, 'Username or Password is incorrect.');
          }
        } else {
          // Handling non-200 status codes
          displayFlashMessage(false, 'An error occurred during login. Please try again later.');
        }
      } catch (error) {
        console.error('Login error:', error);
        displayFlashMessage(false, 'An error occurred during login. Please try again later.');
      }
    };

    // Function to display flash message
    const displayFlashMessage = (success, message) => {
      isSuccess.value = success;
      flashMessage.value = message;
      displayFlash.value = true;
      setTimeout(() => {
        displayFlash.value = false;
      }, 5000); // Hide flash message after 5 seconds
    };

    // Expose reactive variables and functions to the template
    return {
      username,
      password,
      flashMessage,
      displayFlash,
      isSuccess,
      login,
    };
  },
};
</script>
