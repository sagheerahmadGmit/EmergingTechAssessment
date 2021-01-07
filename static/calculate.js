//adapted from https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
getCalculatedTurbinePower = async (otherPrams) => {
    try {
        //fetch the response and the data from the flask api
      const fetchResponse = await fetch(`/calculate/turbine/power`, otherPrams);
      const data = await fetchResponse.json();
      console.log(data)
      //return the predicted data to the user
      return data;
    } catch (e) {
        //catch the errors
      return e;
    }
  }

  //https://stackoverflow.com/questions/58296501/why-does-only-get-request-work-on-frontend-post-put-and-delete-wont-work
  async function calculatePower() {
    var speed = document.getElementById("speed").value

    const otherPrams = {
      body: JSON.stringify({speed: speed}),
      method: "POST"
    }
    //change the power readonly box with the predicted power and output to console for testing purposes
    document.getElementById('power').value = await getCalculatedTurbinePower(otherPrams);
    console.log("Power: " + await getCalculatedTurbinePower(otherPrams))
  }