import { useState } from 'react'
import NavBar from '../Components/NavBar'
import { Button, Card, Container, Form } from 'react-bootstrap'

function Decrypt() {
    const [outputText, setOutputText] = useState("");
    const [isVisible, setIsVisible] = useState(false);

    const handleSubmit = async (e: any) => {
        e.preventDefault();

        const formData: FormData = new FormData(e.target);

        // get the key and the plain text
        const key: string = formData.get('key') as string;
        const cipherText: string = formData.get('cipherText') as string;

        setIsVisible(true);
    }

    return (
        <>
            <NavBar />
            <Container fluid>
                <h1 className='display-6 mt-3'>Decrypt Text</h1>
                <div className='position-absolute top-50 start-50 translate-middle'>
                    <Card style={{ width: "50rem" }}>
                        <Card.Body>
                            <Form method='post' onSubmit={handleSubmit}>
                                <Form.Group className='mb-3'>
                                    <Form.Label>Key</Form.Label>
                                    <Form.Control type='text' name='key' required />
                                </Form.Group>
                                <Form.Group className='mb-3'>
                                    <Form.Label>Cipher Text</Form.Label>
                                    <Form.Control as="textarea" rows={3} cols={50} name='cipherText' required />
                                </Form.Group>
                                <Form.Group className='mb-3'>
                                    <div className="d-grid gap-2">
                                        <Button type='submit' variant='outline-primary'>Decrypt</Button>
                                    </div>
                                </Form.Group>
                            </Form>
                        </Card.Body>
                    </Card>

                    {isVisible && (
                        <Card style={{ width: "50rem" }} className='mb-3 mt-4' id='output'>
                            <Card.Body>
                                <Form.Group className='mt-3'>
                                    <Form.Label>Plain Text</Form.Label>
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

export default Decrypt