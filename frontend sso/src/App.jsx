import React from 'react';
import { GoogleLogin } from 'react-google-login';
import axios from 'axios';

const App = () => {
  const handleLoginSuccess = async (response) => {
    const idToken = response.tokenId;
    console.log('User authenticated:', idToken);
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/google-signin/', {
        id_token: idToken,
      });

      if (res.status === 200) {
        console.log('User authenticated successfully:', res.data);
      } else {
        console.error('Authentication failed:', res.data);
      }
    } catch (error) {
      console.error('Error during authentication:', error);
    }
  };

  const handleLoginFailure = (response) => {
    console.error('Login failed:', response);
  };

  return (
    <div>
      <h2>Google Sign-In Demo</h2>
      <GoogleLogin
        clientId="102041081118-vqnps2p36hei4k87vuqd5m4s6sfkdv52.apps.googleusercontent.com"
        buttonText="Login with Google"
        onSuccess={handleLoginSuccess}
        onFailure={handleLoginFailure}
        cookiePolicy={'single_host_origin'} 
      />
    </div>
  );
};

export default App;
