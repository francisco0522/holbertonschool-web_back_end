// Return a Promise using this prototype function getResponseFromAPI()
function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
      if (true) {
        resolve();
      } else {
        reject();
      }
  });
}

export default getResponseFromAPI;
