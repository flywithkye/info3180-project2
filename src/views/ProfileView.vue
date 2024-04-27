<template>
    <div class="container">
      <div id="profilepg-div">      
        <div id="userinfopg">  
            <div class="box" id="user-info-pic">
                <img alt="Homepage Nature Pic" id="user-photo" src="@/assets/nature_pic.jpg"/>
            </div> 
            <div id="user-info" class="box">
                <h4 id="user-name">Sheamar White</h4>
                <p id="user-location">Kingston, Jamaica</p>
                <p id="user-joined">Member since: January, 2018</p>
                <p id="user-bio ">This is my bio. Kool.</p>
            </div> 
            <div id="user-stats" class="box">
                <div id="followers">
                    <span id="user-follow-num">100</span>
                    <span id="user-followers">Followers</span>
                </div>
                <div id="posts">
                    <span id="user-posts-num">500</span>
                    <span id="user-posts">Posts</span>
                </div>
                <div id="user-buttondiv">
                    <button id="user-button" type="button">Folllow</button>
                </div>
            </div>    
        </div>
        <div id="contentpg">
            <div id="image-div">
                <img alt="Homepage Nature Pic" id="image" src="@/assets/nature_pic.jpg"/>
            </div>
        </div>
    </div>
    </div>
</template>

<style>
  #userinfopg{
    display: grid;
    grid-template-columns: 25% 50% 25%;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    width: 70vw;
    height: 25vh;
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
    width: 14vw;
    height: 25vh;
  }

  #user-info{
    text-align: left;
  }

  #user-name{
    padding-top: 3%;
  }

  #user-stats{
    padding: auto;
  }

  #user-location{
    padding-top: 3%;
  }

  #user-joined{
    margin-top: -15px;
    padding-bottom: 1%;
  }

  #user-stats{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr auto;
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
    background-color: blue;
  }

  #posts{
    display: grid;
    grid-template-rows: auto auto;
    background-color: aqua;
  }

  #user-posts{
    margin-top: -5px;
  }

  #user-follow-num{
    font-weight: bold;
  }

  #user-posts-num{
    font-weight: bold;
    margin-bottom: -15px;
  }

  



</style>