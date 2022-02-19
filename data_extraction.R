production_line_optimization_first_log <- read_delim("Task/production_line_optimization_first_log.csv", delim = ";")
timestamp_raw <- as.data.frame(production_line_optimization_first_log)
str(timestamp_raw)
names(timestamp_raw)[1] <- "ID" 

as.integer(difftime(timestamp_raw$time[2], timestamp_raw$time[1], units = "secs"))

timestamp_A <- timestamp_raw[timestamp_raw$line == "A",]
timestamp_B <- timestamp_raw[timestamp_raw$line == "B",]


timestamp_A1 <- timestamp_A[timestamp_A$module == 1,]
timestamp_A1 <- timestamp_A1[order(timestamp_A1$time),]
timestamp_A2 <- timestamp_A[timestamp_A$module == 2,]
timestamp_A2 <- timestamp_A2[order(timestamp_A2$time),]
timestamp_A3 <- timestamp_A[timestamp_A$module == 3,]
timestamp_A3 <- timestamp_A3[order(timestamp_A3$time),]

timestamp_B1 <- timestamp_B[timestamp_B$module == 1,]
timestamp_B2 <- timestamp_B[timestamp_B$module == 2,]
timestamp_B3 <- timestamp_B[timestamp_B$module == 3,]
timestamp_B4 <- timestamp_B[timestamp_B$module == 4,]
timestamp_B5 <- timestamp_B[timestamp_B$module == 5,]
timestamp_B6 <- timestamp_B[timestamp_B$module == 6,]


getTimes <- function(timestamp_Line_Module){
  data <- data.frame(job_id=0, time=0)
  for (job_id in min(timestamp_Line_Module$job_id):max(timestamp_Line_Module$job_id)) {
    timestamp_Line_Module_Job <- timestamp_Line_Module[timestamp_Line_Module$job_id==job_id,]
    
    startTime <- timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="processing","time"]
    if ("waiting_on_next" %in% timestamp_Line_Module_Job$state) {
      endTime <- timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="waiting_on_next","time"]
    } else {
      endTime <- timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="storing_job","time"]
    }
    fetchTime <- timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="fetching_job","time"]
    
    processingTime <- as.integer(difftime(endTime, startTime, units = "secs"))
    prepTime <- as.integer(difftime(startTime, fetchTime, units = "secs"))
    
    totTime <- processingTime + 2 * prepTime
    data[job_id,] <- c(job_id, totTime[1])
  }
  return(data)
}


getTimesLast <-function(timestamp_Line_Module){
  data <- data.frame(job_id=0, time=0)
  for (job_id in min(timestamp_Line_Module$job_id):(max(timestamp_Line_Module$job_id)-1)) {
    timestamp_Line_Module_Job <- timestamp_Line_Module[timestamp_Line_Module$job_id==job_id,]
    timestamp_Line_Module_Job_next <- timestamp_Line_Module[timestamp_Line_Module$job_id==(job_id+1),] 
    
    startTime <- timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="processing","time"]
    if ("waiting_on_precedent" %in% timestamp_Line_Module_Job_next$state) {
      endTime <- timestamp_Line_Module_Job_next[timestamp_Line_Module_Job_next$state=="waiting_on_precedent","time"]
    } else {
      endTime <- timestamp_Line_Module_Job_next[timestamp_Line_Module_Job_next$state=="fetching_job","time"]
    }
    fetchTime <- timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="fetching_job","time"]
    
    processingFetchTime <- as.integer(difftime(endTime, startTime, units = "secs"))
    prepTime <- as.integer(difftime(startTime, fetchTime, units = "secs"))
    
    totTime <- processingFetchTime + prepTime
    data[job_id,] <- c(job_id, totTime[1])
  }
  data[max(timestamp_Line_Module$job_id),] <- c(max(timestamp_Line_Module$job_id), as.integer(mean(data$time)))
  return(data)
}

A1 <- getTimes(timestamp_A1)
A1$time
A2 <- getTimes(timestamp_A2)
A2$time
A3 <- getTimesLast(timestamp_A3)
A3$time


