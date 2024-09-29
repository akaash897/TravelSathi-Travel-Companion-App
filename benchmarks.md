## On Windows:

1. Download the [Apache benchmark for windows](https://www.apachelounge.com/download/#google_vignette) and 
2. Extract & move the binaries ab.exe and abs.exe to project directory
3. Run the app 
   ```bash
   python app.py
   ```
4. In new terminal, run benchmarking with 100 connection with 1000 requests:
   ```bash
   ab -c 100 -n 1000 http://localhost:5000/
   ```

## References 
1. https://dev.to/gabriellaamah/load-testing-for-api-with-apache-benchmark-on-windows-58oj