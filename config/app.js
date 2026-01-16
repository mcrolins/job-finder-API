import {usestate, useEffect} from 'react';
function App() {
    const [jobs, setJobs] = usestate([]);
    const [loading, setLoading] = usestate(false);
    const [keyword, setKeyword] = usestate('software engineer');
    const [location, setLocation] = usestate('remote');

    const fetchJobs = async () => {
        setLoading(true);
        const res = await fetch(`http://localhost:8000/api/jobs/?q=${keyword}&l=${location}`);
        const data = await res.json();
        setJobs(data.results || []);
        setLoading(false);
    };
    
    useEffect(() => {
        fetchJobs();
    }, []);

    return (
        <div>
            <h1>Job Finder</h1>
            <input onChange={(e) => setKeyword(e.target.value)} placeholder="Job Title" />
            <input onChange={(e) => setLocation(e.target.value)} placeholder="Location" />
            <button onClick={fetchJobs}>Search</button>
            { loading ? <p>Loading...</p> : (
                <div>
                    {jobs.map((job) => (
                        <div key={job.id} style={{ border: '1px solid #ccc', margin: '10px', padding: '10px' }}>
                            <h3>{job.title}</h3>
                            <p>{job.company.display_name}</p>
                            <p>{job.location.display_name}</p>
                            <a href={job.redirect_url} target="_blank">Apply</a>
                        </div>
                    ))}
                </div>
            )}
        </div>
        )
      
}
  export default App;