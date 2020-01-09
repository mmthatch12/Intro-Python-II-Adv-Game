function cutTheSticks(arr) {
    let booly = true
    while(booly){
      let finarr = []
      let copy = [...arr]
      let mini = Math.min(...copy)
      finarr.push(copy.length)
      if(copy.length >= 0){
        copy = copy.map(num => num-mini)
        console.log(copy, mini)
        copy = copy.filter(num => num !== 0)
        mini = Math.min(...copy)
      } else {
        return finarr
        booly = false
      }
      
    }
  
  
  }
  console.log(cutTheSticks([5,4,4,2,2,8]))