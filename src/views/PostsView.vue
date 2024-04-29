<script setup>
    import { ref, onMounted } from "vue"; 
    import PostCard from "@/components/PostCard.vue";

    let posts = ref([]); 
    const error = ref('');
    let loggedIn = false;

    onMounted(() => {
        getUserIdFromToken();       
        fetchPosts();
    });

    function fetchPosts() {
        fetch("http://localhost:8080/api/v1/posts", { 
            method: 'GET',
        }) 
            .then(function (response) { 
                return response.json(); 
            }) 
            .then(function (data) { 
                posts.value = data.data;
                console.log(data); 
            }) 
            .catch(function (error) { 
                console.log(error); 
            });
    }
    

    // Function to extract user ID from token
    function getUserIdFromToken() {
        try {
            // Get the token from local storage
            const token = localStorage.getItem('access_token');
            console.log('Token from local storage:', token);

            if (!token) {
                console.log('No token found in local storage.');
                error.value = "You must be logged in to view all posts.";                  
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

    function isLoggedIn() {
        return loggedIn;
    }

</script>

<template>    
    <main class="container">
        <div id="displayFeedback">
            <div id="loginError" v-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
        </div>

        <div v-if="!isLoggedIn()">     
            <div id="postshider"></div>
            <div id="postshidden">
                <PostCard :post="post" v-for="post in posts" :key="post.id" />
            </div>    
        </div>          
        <div v-else id="posts">
            <PostCard :post="post" v-for="post in posts" :key="post.id" />
        </div>        
    </main>
</template>
  
<style scoped>
    /* Add any component specific styles here */
    #displayFeedback {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        z-index: 2;
        position: fixed;
        top: 80px;
        left: 0; 
        right: 0; 
        margin-left: auto; 
        margin-right: auto; 
    }

    #posts {
        display: grid;
        gap: 50px 30px;
        grid-template-columns: minmax(0, 1fr);  
        padding: 15px 0px 15px 0px;
    }

    #postshidden {
        display: grid;
        gap: 50px 30px;
        grid-template-columns: minmax(0, 1fr);  
        padding: 15px 0px 15px 0px;
        overflow: hidden;
        height: 95vh;
    }

    #postshider {
        background-color: #e9e9e9e0;
        height: 100vh;
        width: 100vw;
        z-index: 1;
        position: fixed;
        top: 0;
        left: 0;
    }

</style>