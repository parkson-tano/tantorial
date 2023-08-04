import {
  TextInput,
  PasswordInput,
  Checkbox,
  Anchor,
  Paper,
  Title,
  Text,
  Container,
  Group,
  Button,
  Box
} from '@mantine/core';
import { Link } from 'react-router-dom';
import { IconAt } from '@tabler/icons-react';
import { useAuth } from '../../context/auth-context';
import { useForm, isNotEmpty, isEmail, isInRange, hasLength, matchesField } from '@mantine/form';


export default function Login() {
  const { login, user } = useAuth();


  const form = useForm({
    initialValues: {
      email: '',
      password: '',
    },

    validate: {
      email: isEmail('Please enter a valid email'),
      password: isNotEmpty('Please enter a password'),
    }
  });

  const handleLogin = async () => {
    const data = {
      email: form.values.email,
      password: form.values.password,

    }
    try {
      await login(data);
    } catch (err) {
      console.log(err);
    }
  }


  console.log(user);
  return (
    <div
      style={{
        backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
      }}
    >
      <Container size={520} my={40}>
        <Box component="form" maw={400} mx="auto" onSubmit={form.onSubmit(handleLogin)}>
        <Title
          align="center"
          sx={(theme) => ({ fontFamily: `Greycliff CF, ${theme.fontFamily}`, fontWeight: 900 })}
        >
          Welcome to Tantorial!
        </Title>
        <Text color="dimmed" size="sm" align="center" mt={5}>
          Do not have an account yet?{' '}
          <Link to="/signup-lander">
            Register
          </Link>
        </Text>

        <Paper withBorder shadow="md" p={30} mt={30} radius="md">
          <TextInput label="User ID/Email" placeholder="you@mantine.dev" 
            {...form.getInputProps('email')}
          />
          <PasswordInput label="Password" placeholder="Your password" mt="md"
          {...form.getInputProps('password')}
          />
          <Group position="apart" mt="lg">
            <Checkbox label="Remember me" />
            <Link to="/forgot-password">Forgot password?</Link>
          </Group>
          <Button fullWidth mt="xl"
          type='submit'
            style={{
              backgroundColor: "#FFC107",
            }}
          >
            Sign in
          </Button>
        </Paper>
        </Box>
      </Container>

    </div>

  );
}