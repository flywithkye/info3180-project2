<template>
    <div class="container">
      <div id="profilepg-div">      
        <div id="userinfopg">  
            <div class="box" id="user-info-pic">
                <img alt="Homepage Nature Pic" id="user-photo" src="@/assets/nature_pic.jpg"/>
            </div> 
            <div id="user-info" class="box">
                <h5 id="user-name">Sheamar White</h5>
                <p id="user-location">Kingston, Jamaica</p>
                <p id="user-joined">Member since: January, 2018</p>
                <p id="user-bio ">This is my bio. Kool.</p>
            </div> 
            <div id="user-stats" class="box">
                <div id="user-stats-inner">
                  <div id="user-followers">
                      <p id="user-follow-num">100</p>
                      <p id="user-followers-name">Followers</p>
                  </div>
                  <div id="user-posts">
                      <p id="user-posts-num">500</p>
                      <p id="user-posts-name">Posts</p>
                  </div>
                </div>
                <div id="user-buttondiv">
                    <button id="user-button" class="btn" type="button">Follow</button>
                </div>
            </div>    
        </div>
        <div id="contentpg">
            <div id="post-card">
                <img alt="Homepage Nature Pic" class="post-image" src="@/assets/nature_pic.jpg"/>
            </div>
            <div id="post-card">
                <img alt="Homepage Nature Pic" class="post-image" src="@/assets/nature_pic.jpg"/>
            </div>
            <div id="post-card">
                <img alt="Homepage Nature Pic" class="post-image" src="@/assets/nature_pic.jpg"/>
            </div>
            <div id="post-card">
                <img alt="Homepage Nature Pic" class="post-image" src="@/assets/nature_pic.jpg"/>
            </div>
        </div>
    </div>
    </div>
</template>

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
    background-color: #d53232;
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
    background-color: aqua;
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