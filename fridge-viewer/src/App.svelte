<script>
  
  async function getData()
  {
    let fridgeContent = await fetch('http://localhost:8000/fridge-items', {
                                    method: 'GET'
                                    })
                              .then(res => res.json())
                              .catch(function(error){console.log(error)})
    console.log(fridgeContent)
    return await fridgeContent
  }

  console.log("TEST")
  let fridgeContent = []
  getData().then(data => (fridgeContent = data['items']))
  console.log(fridgeContent)
  let val = ""
  let date = new Date()
</script>

<main>
  <div>
    <h4>List of items in your fridge:</h4>
  </div>

  {#each fridgeContent as item}
  <div>
    {item.name + " goes bad on " + new Date(item.date).toLocaleDateString()}
  </div>
  {/each}

  <br><br><br><br>

  <div>
    <h4>Add new item:</h4>
    <form on:submit|preventDefault={
        () => 
          fetch('http://localhost:8000/add-new-item', {
                                    method: 'POST',
                                    headers: {
                                      'Content-Type': 'application/json'
                                    },
                                    body: JSON.stringify(
                                    {
                                      'name': val,
                                      'date': new Date(date).getTime()
                                    })})
                              .then(res => res.json())
                              .catch(function(error){console.log(error)})
      }>
      <label for="name"> Enter item name:</label><br>
      <input bind:value={val} id="name"><br><br>
      <label for="date"> Enter item date of expiry:</label>
      <input type="date" bind:value={date} id="date"/><br>
      <input type="submit" value="Submit" id="post-btn">
    </form><br>
    <h4>Add new item based on barcode:</h4>
    <form on:submit|preventDefault={
      () => 
        fetch('http://localhost:8000/add-new-item-with-barcode', {
                                  method: 'POST',
                                  headers: {
                                    'Content-Type': 'application/json'
                                  },
                                  body: JSON.stringify(
                                  {
                                    'name': 'empty',
                                    'date': new Date(date).getTime()
                                  })})
                            .then(res => res.json())
                            .catch(function(error){console.log(error)})
    }>
      <label for="date"> Enter item date of expiry:</label>
      <input type="date" bind:value={date} id="date"/><br>
      <input type="submit" value="Submit" id="post-btn">
    </form>
  </div>

</main>

<style>
  
</style>
