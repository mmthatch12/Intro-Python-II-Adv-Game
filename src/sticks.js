function cutTheSticks(arr) {
    let finarr = []
    let copy = [...arr]
    let mini = Math.min(...copy)
    for(let i = 0;i<arr.length;i++){
      if(copy.length >= 1){
        finarr.push(copy.length)
        copy = copy.map(num => num-mini)
        copy = copy.filter(num => num != 0)
        mini = Math.min(...copy)
      } else {
        break
      }
      
    }
    return finarr
  }
  console.log(cutTheSticks([1,2,3,4,3,3,2,1]))