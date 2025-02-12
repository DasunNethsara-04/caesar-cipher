import { useState } from 'react'
import NavBar from '../Components/NavBar'
import { Button, Card, Container, Form } from 'react-bootstrap'
import axios, { AxiosResponse } from 'axios';

function Encrypt() {
    const [outputText, setOutputText] = useState("");
    const [isVisible, setIsVisible] = useState(false);

    const handleSubmit = async (e: any) => {
        e.preventDefault();

        const formData: FormData = new FormData(e.target);

        // send data to the backend
        try {
            const response: AxiosResponse = await axios.post("http://127.0.0.1:8000/api/enc", formData, {
                headers: {
                    "Content-Type": "application/json",
                },
            });
            if (response.status === 200 || response) {
                console.log(response.data);
            }
        } catch (err) {
            console.error(err);
        }

        setIsVisible(true);
    }

    return (
        <>
            <NavBar />
            <Container fluid>
                <h1 className='display-6 mt-3'>Encrypt Text</h1>
                <div className='position-absolute top-50 start-50 translate-middle'>
                    <Card style={{ width: "50rem" }}>
                        <Card.Body>
                            <Form method='post' onSubmit={handleSubmit}>
                                <Form.Group className='mb-3'>
                                    <Form.Label>Key</Form.Label>
                                    <Form.Control type='text' name='key' required />
                                </Form.Group>
                                <Form.Group className='mb-3'>
                                    <Form.Label>Plain Text</Form.Label>
                                    <Form.Control as="textarea" rows={3} cols={50} name='plainText' required />
                                </Form.Group>
                                <Form.Group className='mb-3'>
                                    <div className="d-grid gap-2">
                                        <Button type='submit' variant='outline-primary'>Encrypt Text</Button>
                                    </div>
                                </Form.Group>
                            </Form>
                        </Card.Body>
                    </Card>

                    {isVisible && (
                        <Card style={{ width: "50rem" }} className='mb-3 mt-4' id='output'>
                            <Card.Body>
                                <Form.Group className='mt-3'>
                                    <Form.Label>Cipher Text</Form.Label>
                                    <Form.Control as="textarea" rows={3} cols={50} name='outputText' readOnly />
                                </Form.Group>
                            </Card.Body>
                        </Card>
                    )}
                </div>
            </Container>
        </>
    )
}

export default Encrypt